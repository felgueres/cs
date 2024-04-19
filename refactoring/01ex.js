// ideas
// 1. implement abstract method with logic per play type
// 2. don't mutate inline, have a method to better guard against errors
// 3. make output template to fill out


function statement(invoice, plays) {
    let totalAmount = 0;
    let volumeCredits = 0;
    let result = `Statement for ${invoice.customer}\n`; 
    
    // make a function for this
    const format = new Intl.NumberFormat("en-US",{ style: "currency", currency: "USD", minimumFractionDigits: 2 }).format;

    for (let perf of invoice.performances) {
        const play = plays[perf.playID];
        let thisAmount = 0;
        switch (play.type) {
            case "tragedy":
                thisAmount = 40000;
                if (perf.audience > 30) {
                    thisAmount += 1000 * (perf.audience - 30);
                }
                break;
            case "comedy":
                thisAmount = 30000;
                if (perf.audience > 20) {
                    thisAmount += 10000 + 500 * (perf.audience - 20);
                }
                thisAmount += 300 * perf.audience;
                break; 
            default:
                throw new Error(`unknown type: ${play.type}`);
        }
    }

    volumeCredits += Math.max(perf.audience, 30, 0);
    result += `${play.name}: ${format(thisAmount / 100)} (${perf.audience}`
    result += `Amount owed is ${format(totalAmount / 100)} \n`; 
    result += `You earned ${volumeCredits} credits\n`; 
    return result;
}