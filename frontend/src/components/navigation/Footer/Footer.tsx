import React from "react";

export type IFooter = React.ComponentPropsWithoutRef<"footer">;

export default function Footer({ className, ...footerProps }: IFooter) {
    return (
        <footer
            {...footerProps}
            className={`text-center w-full p-5 ${className}`}
        ></footer>
    );
}
