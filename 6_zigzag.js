const solution = function(s, numRows) {
    dict = {}
    down = true
    c = 0
    if (numRows==1) return s

    for (i=0;i<s.length;i++){
        if(down){
            dict[c] = !dict[c] ? s[i] : dict[c] + s[i]
            c++
            // console.log(dict)
        }
        else{
            dict[c] = dict[c] + s[i]
            c--
            // console.log(dict)
        }
        if (c==numRows){
            down = false
            c=numRows-2
        }
        if (c==-1){
            down = true
            c=1
        }
    }
    // final=""
    // for(key in dict){
    //     final += dict[key]
    // }
    var final = Object.keys(dict).map(key => `${dict[key]}`).join("");
    return final 
};

console.log(solution("PAYPALISHIRING",3))