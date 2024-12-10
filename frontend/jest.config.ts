import type { Config } from "@jest/types";
import nextJest from "next/jest.js";

const createJestConfig = nextJest({
    dir: "./",
});

const config: Config.InitialOptions = {
    preset: "ts-jest",
    testEnvironment: "jsdom",
    coverageProvider: "v8",
    collectCoverage: true,
    coverageDirectory: "coverage",
    moduleNameMapper: {
        "^@/(.*)$": "<rootDir>/$1",
    },
    moduleDirectories: ["node_modules", "<rootDir>/"],
    injectGlobals: true,
    setupFilesAfterEnv: ["./jest.setup.ts"],
};

export default createJestConfig(config);
