import { NextPageWithLayout } from "@/pages/page";
import { LoaderCircle } from "lucide-react";
import PrimaryLayout from "../PrimaryLayout";

const LoadingPage: NextPageWithLayout = () => {
    return (
        <div className="flex items-center justify-center">
            <h2 className="mr-2 text-xl">Loading</h2>
            <LoaderCircle className="animate-spin" />
        </div>
    );
};

LoadingPage.getLayout = (page) => {
    return <PrimaryLayout>{page}</PrimaryLayout>;
};

export default LoadingPage;
