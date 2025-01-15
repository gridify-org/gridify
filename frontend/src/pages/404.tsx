import PrimaryLayout from "@/components/layouts/PrimaryLayout";
import { NextPageWithLayout } from "@/pages/page";

const NotFound: NextPageWithLayout = () => {
    return <h2 className="font-bold text-2xl mb-4">Page Not Found</h2>;
};

export default NotFound;

NotFound.getLayout = (page) => {
    return <PrimaryLayout>{page}</PrimaryLayout>;
};
