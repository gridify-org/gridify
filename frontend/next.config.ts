import type { NextConfig } from "next";

const nextConfig: NextConfig = {
    webpack: (config) => {
        config.module.rules.push({
            test: /\.test\.tsx$/,
            use: "ignore-loader",
        });

        return config;
    },
};

export default nextConfig;
