import { Link, Outlet, useNavigate } from "react-router-dom";

export default function Layout() {
    const navigate = useNavigate();

    const logout = () => {
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        navigate("/login");
    };

    return (
        <div className="container-fluid">
            <div className="row">

                {/* SIDEBAR */}
                <div className="col-2 bg-dark text-white min-vh-100 p-3">
                    <h5>Меню</h5>
                    <hr />

                    <Link className="text-white d-block mb-2" to="/">
                        Главная
                    </Link>

                    <Link className="text-white d-block mb-2" to="/books">
                        Книги
                    </Link>

                    <Link className="text-white d-block mb-2" to="/profile">
                        Профиль
                    </Link>

                    <hr />

                    <button className="btn btn-outline-light w-100" onClick={logout}>
                        Выйти
                    </button>
                </div>

                {/* CONTENT */}
                <div className="col-10 p-4">
                    <Outlet />
                </div>

            </div>
        </div>
    );
}
