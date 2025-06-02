function treat_exp(raw_r): number {
    if ("*" in raw_r) {
        let parts = raw_r.split("*");
        let base_value = parseFloat(parts[0]);
        let exponent = parts[1];
        let exp_parts = exponent.split("^",1);
        let power = parseInt(exp_parts[1])
        exponent = 10**power;

        let calculated_value = base_value * exponent;

        return calculated_value;
    } else {
        let calculated_value = parseFloat(raw_r);
        return calculated_value;
    }
}

class Ohm {
    raw_r: string;
    raw_v: string;
    raw_i: string;
    r: number;
    v: number;
    i: number;
    diameter: number;
    a: number;
    l: number;
    
    constructor(raw_r: string, raw_v: string, raw_i: string, diameter: number, a: number, l: number) {
        this.raw_r = raw_r;
        this.raw_v = raw_v;
        this.raw_i = raw_i;
        this.diameter = diameter;
        this.a = a;
        this.l = l;

        this.r = treat_exp(raw_r);
        this.v = treat_exp(raw_v);
        this.i = treat_exp(raw_i);
    }

    voltage(r:number, i:number): number {
        return r * i;
        
    }

    amperage(v:number, r:number): number {
        return v / r;
    }

    resistance(v:number, i:number): number {
        return v / i;
    }
};