import Head from "next/head";
import React from "react";

import Footer from "@/components/navigation/Footer";
import Header from "@/components/navigation/Header";
import { cn } from "@/lib/utils";
import musicService from "@/services/music/service";

export interface IPrimaryLayout extends React.ComponentPropsWithoutRef<"div"> {
    mainClassName?: string;
    title?: string;
}

function PrimaryLayout({
    children,
    mainClassName,
    title,
    ...divProps
}: IPrimaryLayout) {
    return (
        <>
            <Head>
                <title>Gridify</title>
            </Head>
            <div {...divProps} className="flex flex-col min-h-[98vh]">
                <Header musicService={musicService} />
                <main
                    className={cn(
                        "flex-grow w-1/2 mx-auto mt-10 min-w-[600px]",
                        mainClassName
                    )}
                >
                    {title && (
                        <h2 className="font-bold text-2xl mb-4">{title}</h2>
                    )}
                    {children}
                </main>
                <div className="m-auto" />
                <Footer />
            </div>
        </>
    );
}

export default PrimaryLayout;
