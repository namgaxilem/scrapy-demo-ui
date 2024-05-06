import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./App.css";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Home from "./pages/Home";
import Address from "./pages/Address";
import Policy from "./pages/Policy";
import Notification from "./pages/Notification"
import Login from "./pages/Login"

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/about",
    element: <About />,
  },
  {
    path: "/contact",
    element: <Contact />,
  },
  {
    path: "/address",
    element: <Address />,
  },
  {
    path: "/policy",
    element: <Policy />,
  },
  {
    path: "/notification",
    element: <Notification />
  },
  {
    path: "/login",
    element: <Login />
  }
]);

function App() {
  return (
    <>
      <React.StrictMode>
        <RouterProvider router={router} />
      </React.StrictMode>
    </>
  );
}

export default App;
