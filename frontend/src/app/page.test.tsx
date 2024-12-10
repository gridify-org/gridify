import React from "react";
import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import Home from "./page";

describe("renders Welcome to Gridify text", () => {
    it("renders Welcome to Gridify text", () => {
        render(<Home />);
        const welcomeElement = screen.getByText(/Welcome to Gridify/i);
        expect(welcomeElement).toBeInTheDocument();
    });
});
