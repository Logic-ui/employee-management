from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Employee

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def home():
    return "API is running"


@app.route("/employees", methods=["GET"])
def get_employees():
    employees = Employee.query.all()
    return jsonify(
        [
            {
                "id": emp.id,
                "name": emp.name,
                "email": emp.email,
                "position": emp.position,
                "salary": emp.salary,
            }
            for emp in employees
        ]
    )


@app.route("/employee", methods=["POST"])
def add_employee():
    data = request.json
    emp = Employee(
        name=data["name"],
        email=data["email"],
        position=data["position"],
        salary=data["salary"],
    )
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "Employee added"})


@app.route("/employee/<int:id>", methods=["PUT"])
def update_employee(id):
    data = request.json
    emp = Employee.query.get(id)

    if not emp:
        return jsonify({"message": "Not found"}), 404

    emp.name = data["name"]
    emp.email = data["email"]
    emp.position = data["position"]
    emp.salary = data["salary"]

    db.session.commit()
    return jsonify({"message": "Employee updated"})


@app.route("/employee/<int:id>", methods=["DELETE"])
def delete_employee(id):
    emp = Employee.query.get(id)

    if not emp:
        return jsonify({"message": "Not found"}), 404

    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Employee deleted"})


if __name__ == "__main__":
    with app.app_context():
        print("Creating database...")
        db.create_all()
        print("Database created successfully.")
    app.run(debug=True)
