import ErrorOccurredPage from "@/components/layouts/ErrorOccurredPage";
import LoadingPage from "@/components/layouts/LoadingPage";
import { Input } from "@/components/ui/input";
import { ISearchArtist } from "@/services/music/serviceInterfaces";
import { useQuery } from "@tanstack/react-query";
import { useEffect, useState } from "react";
import { LoaderCircle } from "lucide-react";
import { ArtistSearchResponse } from "@/schemas/artist";
import { cn } from "@/lib/utils";

interface SearchResultsProps {
    results: ArtistSearchResponse;
    maxSize?: number;
}

const SearchResults = ({ results, maxSize = 10 }: SearchResultsProps) => {
    const artists = results.results.artistmatches.artist.slice(0, maxSize);

    return (
        <div className="absolute w-full mt-1 bg-popover rounded-md shadow-lg border border-input ring-1 ring-ring">
            <ul className="py-1">
                {artists.length > 0 ? (
                    artists.map((artist) => (
                        <li
                            key={artist.mbid || artist.name}
                            className="px-4 py-2 hover:bg-secondary cursor-pointer"
                        >
                            {artist.name}
                        </li>
                    ))
                ) : (
                    <li className="px-4 py-2 text-muted-foreground">
                        No results found
                    </li>
                )}
            </ul>
        </div>
    );
};

interface ISearchBarProps {
    className?: string;
    musicService: ISearchArtist;
}

export default function SearchBar({
    musicService,
    className,
    ...props
}: ISearchBarProps) {
    const [searchTerm, setSearchTerm] = useState("");
    const [isFocused, setIsFocused] = useState(false);

    const { data: searchResults, isLoading } = useQuery({
        queryKey: ["artistSearch", searchTerm],
        queryFn: () => musicService.search(searchTerm),
        enabled: searchTerm.length > 0,
    });

    const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
        setSearchTerm(e.target.value);
    };

    useEffect(() => {
        console.log(searchResults);
    }, [searchResults]);

    return (
        <div className={cn("relative w-80", className)} {...props}>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                className="absolute top-0 bottom-0 w-6 h-6 my-auto text-white left-3"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                />
            </svg>
            <Input
                type="text"
                placeholder="Search"
                className="pl-12 pr-4"
                onChange={handleSearch}
                onFocus={() => setIsFocused(true)}
                onBlur={() => setIsFocused(false)}
            />
            {isLoading && (
                <LoaderCircle className="absolute top-0 bottom-0 my-auto right-3 animate-spin" />
            )}
            {searchResults && searchTerm.length > 0 && isFocused && (
                <SearchResults results={searchResults} maxSize={10} />
            )}
        </div>
    );
}
