from infrastructure.database import Database
from infrastructure.student_repository import StudentRepository
from usecases.student_usecase import StudentUseCase
from presentation.views.student_view import StudentView
from presentation.controllers.student_controller import StudentController


def main():
    # 1. Initialize Database
    db = Database(
        host="localhost",
        user="root",
        password="",
        database="db_kampus"
    )

    # 2. Initialize Repository
    repo = StudentRepository(db)

    # 3. Initialize Use Case
    usecase = StudentUseCase(repo)

    # 4. Initialize View and Controller
    view = StudentView()
    controller = StudentController(usecase, view)

    # 5. Load Data and Run
    controller.load_students()
    view.mainloop()


if __name__ == "__main__":
    main()