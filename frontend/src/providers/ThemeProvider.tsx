import React, { useEffect, useMemo, useState } from "react";

import { ThemeProviderContext } from "@/context/ThemeContext";
import { Theme } from "@/types/Theme";

interface ThemeProviderProps {
    children: React.ReactNode;
    defaultTheme: Theme;
    storageKey: string;
}

export default function ThemeProvider({
    children,
    defaultTheme = "system",
    storageKey = "theme",
    ...props
}: ThemeProviderProps) {
    const [theme, setTheme] = useState<Theme>(
        () =>
            (typeof window !== "undefined"
                ? (window.sessionStorage.getItem(storageKey) as Theme)
                : defaultTheme) || defaultTheme
    );

    useEffect(() => {
        const root = window.document.documentElement;

        root.classList.remove("light", "dark");

        if (theme === "system") {
            const systemTheme = window.matchMedia(
                "(prefers-color-scheme: dark)"
            ).matches
                ? "dark"
                : "light";
            root.classList.add(systemTheme);
            return;
        }

        root.classList.add(theme);
    }, [theme]);

    const value = useMemo(
        () => ({
            theme,
            setTheme: (newTheme: Theme) => {
                window.sessionStorage.setItem(storageKey, newTheme);
                setTheme(newTheme);
            },
        }),
        [theme, storageKey]
    );

    return (
        <ThemeProviderContext.Provider {...props} value={value}>
            {children}
        </ThemeProviderContext.Provider>
    );
}
