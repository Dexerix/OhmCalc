function treat_exp(raw_r: string): number {
    if (raw_r.indexOf("*") !== -1) {
        let parts = raw_r.split("*");
        let base_value = parseFloat(parts[0]);
        let exponent = parts[1];
        let exp_parts = exponent.split("^");
        let power = parseInt(exp_parts[1])
        let exponent_value = 10**power;

        let calculated_value = base_value * exponent_value;

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
        let v = r * i;
        return v;
    }

    amperage(v:number, r:number): number {
        let a = v / r;
        return a;
    }

    resistance(v:number, i:number): number {
        let r = v / i;
        return r;
    }
};