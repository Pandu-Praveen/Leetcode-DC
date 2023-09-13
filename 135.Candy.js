var candy = function(ratings) {
    let total = ratings.length;
    let pandu = Array(total).fill(1);

    for(let i = 1; i < total; i++){
        if(ratings[i-1] < ratings[i]){
            pandu[i] = pandu[i-1] + 1;
        }
    }

    for(let i = total-2; i >= 0; i--){
        if(ratings[i] > ratings[i+1] && pandu[i] <= pandu[i+1]){
            pandu[i] = pandu[i+1] + 1;
        }
    }

    return pandu.reduce((a,b) => a + b)
};