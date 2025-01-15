import React from "react";

import SearchBar from "@/components/common/SearchBar/SearchBar";
import {
    NavigationMenu,
    NavigationMenuItem,
    NavigationMenuList,
} from "@/components/ui/navigation-menu";
import { ISearchArtist } from "@/services/music/serviceInterfaces";

export type IHeader = React.ComponentPropsWithoutRef<"header"> & {
    musicService: ISearchArtist;
};

export default function Header({ musicService, ...headerProps }: IHeader) {
    return (
        <header {...headerProps}>
            <NavigationMenu className="ml-auto">
                <NavigationMenuList>
                    <NavigationMenuItem>
                        <SearchBar
                            musicService={musicService}
                            className="m-3"
                        />
                    </NavigationMenuItem>
                </NavigationMenuList>
            </NavigationMenu>
        </header>
    );
}
