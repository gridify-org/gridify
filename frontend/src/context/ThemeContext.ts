import { createContext, useContext } from "react";

import { Theme } from "@/types/Theme";

interface ThemeProviderState {
    theme: Theme;
    setTheme: (_theme: Theme) => void;
}

const initialState: ThemeProviderState = {
    theme: "system",
    setTheme: () => null,
};

export const ThemeProviderContext =
    createContext<ThemeProviderState>(initialState);

export const useTheme = () => {
    const context = useContext(ThemeProviderContext);

    if (context === undefined)
        throw new Error("useTheme must be used within a ThemeProvider");

    return context;
};
