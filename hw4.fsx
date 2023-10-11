//how to execute .fsx file: select paragraph && press option+return

//Exercise 1
let rec maxGrade grades =
    let rec calculateWeightedGrade (p, a, m, f) =
        (p * 0.05) + (a * 0.45) + (m * 0.25) + (f * 0.25)
    
    let rec innerMaxGrade grades cur =
        match grades with
        //if empty list
        | [] -> cur
        //recursively compute grade from tuple
        | x::rest ->
            let grade = calculateWeightedGrade x
            if grade > cur then
                innerMaxGrade rest grade
            else
                innerMaxGrade rest cur
    
    match grades with
    //if empty list
    | [] -> 0.0
    | _ -> innerMaxGrade grades 0.0

//output test all correct
maxGrade [(90.0, 75.0, 82.5, 89.0);(85.5, 82.0, 72.5, 92.0)] ;; 
//val it: float = 82.3 
maxGrade [(60.0, 70.0, 80.0, 90.0)] ;; 
//val it : float = 77.0 


//Exercise 2
let rec makeAscend list =
    match list with
    //base case:if empty
    | [] -> []
    //base case:only 1 element
    | [x] -> [x]
    //recursive case with 2+ elements
    | x :: y :: rest ->
        if x <= y 
            then x :: makeAscend (y :: rest)
            else makeAscend (x :: rest)

makeAscend [1; 4; 2; 7; 6; 3; 5; 9; 8] ;; 
//val it: int list = [1; 4; 7; 9] 
makeAscend [1; 4; 4; 0; 0; 6; 1; 8] ;; 
//val it: int list = [1; 4; 4; 6; 8] 

//Exercise 3

type PairBST =
   | Empty
   | TreeNode of string * float * PairBST * PairBST


let rec insert v1 v2 = function
    //if empty
   | Empty -> TreeNode (v1, v2, Empty, Empty)
   | TreeNode (k, v, left, right) ->
       if v2 = v then
           TreeNode (k, v, left, right)
       elif v2 < v then
           TreeNode (k, v, insert v1 v2 left, right)
       else
           TreeNode (k, v, left, insert v1 v2 right)


let rec search v1 v2 = function
   | Empty -> false
   | TreeNode (k, v, left, right) ->
       if v2 = v && v1 = k then
           true
       elif v2 < v then
           search v1 v2 left
       else
           search v1 v2 right


let rec count func = function
   | Empty -> 0
   | TreeNode (k, v, left, right) ->
       let left_count = count func left
       let right_count = count func right
       let node_count = if func (k, v) then 1 else 0
       left_count + right_count + node_count

let bt1 = insert "juice" 3.99 Empty;; 
//val bt1: PairBST = TreeNode ("juice", 3.99, Empty, Empty) 
 
let bt2 = insert "cup" 1.25 bt1;; 
//val bt2: PairBST = 
 // TreeNode ("juice", 3.99, TreeNode ("cup", 1.25, Empty, Empty), Empty) 
 
let bt3 = insert "blanket" 12.50 bt2;; 
//val bt3: PairBST = 
  //TreeNode 
    //("juice", 3.99, TreeNode ("cup", 1.25, Empty, Empty), 
     //TreeNode ("blanket", 12.5, Empty, Empty)) 
 
let bt4 = insert "table" 17.75 bt3;; 
// val bt4: PairBST = 
//   TreeNode 
//     ("juice", 3.99, TreeNode ("cup", 1.25, Empty, Empty), 
//      TreeNode 
//        ("blanket", 12.5, Empty, TreeNode ("table", 17.75, Empty, Empty))) 
 
let bt5 = insert "pen" 2.67 bt4;; 
// val bt5: PairBST = 
//   TreeNode 
//     ("juice", 3.99, 
//      TreeNode ("cup", 1.25, Empty, TreeNode ("pen", 2.67, Empty, Empty)), 
//      TreeNode 
//        ("blanket", 12.5, Empty, TreeNode ("table", 17.75, Empty, Empty))) 
 
search "cup" 1.25 bt5;; 
//val it: bool = true 
 
search "table" 2.67 bt5;; 
//val it: bool = false 
 
count (fun (s,f) -> f < 5.0) bt5;; 
//val it: int = 3 
 
count (fun (x,y) -> x.[1] = 'u') bt5;; 
//val it: int = 2
