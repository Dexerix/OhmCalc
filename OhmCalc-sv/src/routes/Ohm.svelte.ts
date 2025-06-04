let raw_r: string;
let raw_v: string;
let raw_i: string;
let r: number;
let v: number;
let i: number;
let diameter: number;
let a: number;
let l: number;

function treat_exp(raw_v: string): number {
    if (raw_v.indexOf("*") !== -1) {
        let parts = raw_v.split("*");
        let base_value = parseFloat(parts[0]);
        let exponent = parts[1];
        let exp_parts = exponent.split("^");
        let power = parseInt(exp_parts[1])
        let exponent_value = 10**power;

        let calculated_value = base_value * exponent_value;

        return calculated_value;
    } else {
        let calculated_value = parseFloat(raw_v);
        return calculated_value;
    }
};

export function voltage(raw_r:string, raw_i:string): number {
        r = treat_exp(raw_r);
        i = treat_exp(raw_i)
        v = r * i;
        return v;
};

export function amperage(v:number, r:number): number {
        let a = v / r;
        return a;
};

export function resistance(v:number, i:number): number {
        let r = v / i;
        return r;
};