// main.tsx or main.jsx
import React from "react";
import ReactDOM from "react-dom/client";
import { NextUIProvider } from "@nextui-org/react";
import App from "./App";
import "./index.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <React.StrictMode>
      <NextUIProvider>
        <Routes>
          <Route path="/chat" element={<App />} />
        </Routes>
      </NextUIProvider>
    </React.StrictMode>
  </BrowserRouter>
);
