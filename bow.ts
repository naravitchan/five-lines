class Bow {
    data = "";
    private data2 = 0;
    constructor(data: string, data2: number) {
        this.data = data;
        this.data2 = data2;
    }
}

class Bow2 {
    // data = "";
    // private data2 = 0;
    constructor(public data: string, private data2: number) {
        // this.data = data;
        // this.data2 = data2;
    }
}