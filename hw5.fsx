//3400-hw5
//txia@seattleu.edu

type Expression = 
    | Complex of int * int 
    | Neg of Expression 
    | Add of Expression * Expression 
    | Sub of Expression * Expression 
    | Mul of Expression * Expression 

//a
let rec toString (expr:Expression) = 
    match expr with
    | Complex (r, i) ->
        //if both real & imagine# == 0
        if r = 0 && i = 0 then "0"
        //if real = 0 && imagine is negative#
        else if r = 0 && i < 0 then "-" + toString (Complex (0, -i)) + "i"
        //if real = 0 && imagine is normal positive int
        else if r = 0 then toString (Complex (i, 0)) + "i"
        //if imagine = 0 && real is normal positive int
        else if i = 0 then  string r 
        //if imagine is negative && real is normal positive int
        else if i < 0 then string r + " - " + toString (Complex (0, -i)) + "i"
        //avoid 1i
        else if i = 1 then string r + " + i"
        //bothe normal positive int
        else string r + " + " + string i + "i"
        |Neg ex -> "-(" + toString(ex) + ")"
        |Add (u, v) ->  "((" + toString(u) + ")+" + "(" + toString(v) + "))"
        |Sub (j, k) -> "(" + toString(j) + " - " + toString(k) + ")"
        |Mul (p, q) -> 
            match (p, q) with
            | Neg a, b ->  toString(p) + "*(" + toString(q) + ")"
            | a, Neg b -> "(" + toString(p) + ")*" + toString(q)
            | Complex (r, i), Complex (s, t) ->
                if i = 0 && t = 0 then "(" + string r + ")*" + string s
                elif i = 0 then "(" + string r + ")*" + toString(q)
                elif t = 0 then toString(p) + "*" + "(" + string s + ")"
                else toString(p) + "*" + toString(q)
            | _, _ ->  toString(p) + "*" + toString(q)
//output all correct
// let expr1 = Complex(3,2)
// toString expr1
// let expr2 = Neg(Complex (3, 2)) // "-(3 + 2i)" 
// toString expr2
// let expr3 = Add(Complex (3, 1), Complex (2, 4)) //"((3 + i)+(2 + 4i))" 
// toString expr3
// let expr4 =Neg(Mul(Complex (3, 0), Neg(Complex (2, 4)))) // "-((3)*-(2 + 4i))" 
// toString expr4
// let expr5 = Mul (Complex (3, 0), Complex (2, 4))
// toString expr5


//b
let rec evaluate (expr:Expression) = 
    match expr with
    | Complex (r, i) -> Complex (r, i)
    //if negation, evaluate arg and negate value
    | Neg ex -> 
        let simplified = evaluate ex
        match simplified with
        | Complex (r, i) -> Complex (-r, -i)
        | _ -> failwith "Invalid expression"
     //if addition, evaluate both arg and add their values
    | Add (u, v) -> 
        let simplifiedU = evaluate u
        let simplifiedV = evaluate v
        match (simplifiedU, simplifiedV) with
        | Complex (r1, i1), Complex (r2, i2) -> Complex (r1 + r2, i1 + i2)
        | _, _ -> failwith "Invalid expression"
    //if subtraction, evaluate both arg and subtract their values
    | Sub (j, k) -> 
        let simplifiedJ = evaluate j
        let simplifiedK = evaluate k
        match (simplifiedJ, simplifiedK) with
        | Complex (r1, i1), Complex (r2, i2) -> Complex (r1 - r2, i1 - i2)
        | _, _ -> failwith "Invalid expression"
    //if multiplication, evaluate both args and multiply values
    | Mul (p, q) -> 
        let simplifiedP = evaluate p
        let simplifiedQ = evaluate q
        match (simplifiedP, simplifiedQ) with
        | Complex (r1, i1), Complex (r2, i2) -> 
            let real = r1 * r2 + i1 * i2 * -1
            let imaginary = r1 * i2 + i1 * r2
            Complex (real, imaginary)
        | _, _ -> failwith "Invalid expression"
//output all correct

//c
let isConjugate (expr1:Expression) (expr2:Expression) =
    match (expr1, expr2) with
    //check if both are complex with equal real && oppisite imaginary 
    | Complex (r1, i1), Complex (r2, i2) when r1 = r2 && i1 = -i2 ->
        let product = Mul(expr1, expr2)
        Some (evaluate product)
    | _ -> None
//output all correct