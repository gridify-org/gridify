import PrimaryLayout from "@/components/layouts/PrimaryLayout";
import { NextPageWithLayout } from "@/pages/page";

const Home: NextPageWithLayout = () => {
    return <div>Welcome to Gridify</div>;
};

Home.getLayout = (page) => {
    return <PrimaryLayout>{page}</PrimaryLayout>;
};

export default Home;
