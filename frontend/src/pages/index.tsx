import PrimaryLayout from "@/components/layouts/PrimaryLayout";
import { NextPageWithLayout } from "@/pages/page";

const Home: NextPageWithLayout = () => {
    return <div>Home</div>;
};

export default Home;

Home.getLayout = (page) => {
    return <PrimaryLayout>{page}</PrimaryLayout>;
};
