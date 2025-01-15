export interface ArtistSearchResponse {
    results: Results;
}

export interface Results {
    artistmatches: ArtistMatches;
}

export interface ArtistMatches {
    artist: ArtistSearchResult[];
}

export interface ArtistSearchResult {
    image: Image[];
    listeners: string;
    mbid: string;
    name: string;
    streamable: string;
    url: string;
}

export interface Image {
    "#text": string;
    size: string;
}

export interface ArtistGetResponse {
    artist: ArtistGetResponseArtist;
}

export interface ArtistGetResponseArtist {
    bio: Bio;
    image: Image[];
    mbid: string;
    name: string;
    ontour: string;
    similar: SimilarArtists;
    stats: Stats;
    streamable: string;
    tags: Genres;
    url: string;
}

export interface Bio {
    content: string;
    links: Links;
    published: string;
    summary: string;
}

export interface Links {
    link: Link;
}

export interface Link {
    "#text": string;
    href: string;
    rel: string;
}

export interface SimilarArtists {
    artist: ArtistElement[];
}

export interface ArtistElement {
    name: string;
    url: string;
}

export interface Stats {
    listeners: string;
    playcount: string;
}

export interface Genres {
    tag: Genre[];
}

export interface Genre {
    name: string;
    url: string;
}
