import React from "react";

export type IHeader = React.ComponentPropsWithoutRef<"header">;

export default function Header({ ...headerProps }: IHeader) {
    return <header {...headerProps}></header>;
}
