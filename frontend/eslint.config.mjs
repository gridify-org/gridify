import tseslint from "typescript-eslint";
import jest from "eslint-plugin-jest";
import eslint from "@eslint/js";

export default tseslint.config({
    languageOptions: {
        globals: {
            jest: true,
            "jest/globals": true,
            React: "readonly",
        },
    },
    files: ["**/*{.ts,.tsx,.js,.jsx}"],
    ignores: [
        "src/components/ui/**/*",
        ".next/**/*",
        "node_modules/**/*",
        "**/*.d.ts",
    ],
    plugins: {
        jest: jest,
    },
    extends: [
        eslint.configs.recommended,
        ...tseslint.configs.recommended,
        ...tseslint.configs.stylistic,
    ],
});
