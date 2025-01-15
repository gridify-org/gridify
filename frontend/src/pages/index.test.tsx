import { render, screen } from "@testing-library/react";
import React from "react";

import Home from "./index";

describe("Home page", () => {
    it("renders Welcome to Gridify text", () => {
        render(<Home />);
        const welcomeElement = screen.getByText(/Welcome to Gridify/i);
        expect(welcomeElement).toBeInTheDocument();
    });
});
