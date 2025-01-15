import tseslint from "typescript-eslint";
import jest from "eslint-plugin-jest";
import unusedImports from "eslint-plugin-unused-imports";
import simpleImportSort from "eslint-plugin-simple-import-sort";

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
        "unused-imports": unusedImports,
        "simple-import-sort": simpleImportSort,
    },
    extends: [
        eslint.configs.recommended,
        ...tseslint.configs.recommended,
        ...tseslint.configs.stylistic,
        eslint.configs.jest,
    ],
    rules: {
        "simple-import-sort/imports": "error",
        "simple-import-sort/exports": "error",
        "no-unused-vars": [
            "warn",
            {
                args: "after-used",
                argsIgnorePattern: "^_",
            },
        ],
        "unused-imports/no-unused-imports": "error",
        "unused-imports/no-unused-vars": [
            "warn",
            {
                vars: "all",
                varsIgnorePattern: "^_",
                args: "after-used",
                argsIgnorePattern: "^_",
            },
        ],
        "@typescript-eslint/no-unused-vars": [
            "warn",
            {
                args: "after-used",
                argsIgnorePattern: "^_",
            },
        ],
    },
});
