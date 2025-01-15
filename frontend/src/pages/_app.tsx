import "./globals.css";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import type { AppProps } from "next/app";

import ThemeProvider from "@/providers/ThemeProvider";

import { NextPageWithLayout } from "./page";
import musicService from "@/services/music/service";
import backendService from "@/services/backend/service";

const queryClient = new QueryClient();

interface AppPropsWithLayout extends AppProps {
    Component: NextPageWithLayout;
}

const services = {
    musicService: musicService,
    backendService: backendService,
};

function MyApp({ Component, pageProps }: AppPropsWithLayout) {
    const getLayout = Component.getLayout || ((page) => page);

    pageProps = { ...pageProps, ...services };

    return (
        <QueryClientProvider client={queryClient}>
            <ThemeProvider defaultTheme="dark" storageKey="theme">
                {getLayout(<Component {...pageProps} />)}
            </ThemeProvider>
        </QueryClientProvider>
    );
}

export default MyApp;
