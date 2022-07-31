const puppeteer = require("puppeteer-extra");
const pluginStealth = require("puppeteer-extra-plugin-stealth");
puppeteer.use(pluginStealth());

function searchFormat(arg) {
    let puncList = "¬`!\"£$%^&*()_-+={[}]:;@'~#<,>.?/\\|";
    puncList = puncList.split("");
    let word = "";
    let temp = arg;
    let i = 0;
    for (let letter = temp[i]; i < temp.length; letter = temp[i]) {
        if (letter == " ") {
            word += "-";
        } else if (!(puncList.includes(letter))) {
            word += letter;
        }
        i++;
    }
    return word;
}

async function scrapeImageMTG(name, set) {
    const formatName = searchFormat(name);
    const formatSet = searchFormat(set);

    url = "https://www.cardmarket.com/en/Magic/Products/Singles/" + formatSet + "/" + formatName;

    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();
    const navigationPromise = page.waitForNavigation({waitUntil: "domcontentloaded"});
    await page.goto(url);
    
    await navigationPromise;
    const [el] = await page.$x('//*[@id="image"]/div/div/div[2]/div/img');
    const src = await el.getProperty("src");
    const image = src.jsonValue();
    
    console.log({image});

    browser.close();
}

async function scrapePriceMTG(name, set, foilVariance) {
    const formatName = searchFormat(name);
    const formatSet = searchFormat(set);

    let url = "";
    if (foilVariance === "Non Foil") {
        url = "https://www.cardmarket.com/en/Magic/Products/Singles/" + formatSet + "/" + formatName;
    } else {
        url = "https://www.cardmarket.com/en/Magic/Products/Singles/" + formatSet + "/" + formatName + "?isFoil=Y";
    }


    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();
    const navigationPromise = page.waitForNavigation({waitUntil: "domcontentloaded"});
    await page.goto(url);
    
    await navigationPromise;
    const [el] = await page.$x('//*[@id="tabContent-info"]/div/div[2]/div/div[2]/dl/dd[9]/span');
    const text = await el.getProperty("textContent");
    const price = text.jsonValue();
    
    console.log({price});
    tempPrice = price;
    console.log(tempPrice);

    browser.close();

    return tempPrice;
}

scrapeImageMTG("Llanowar Elves", "Alpha");
console.log(scrapePriceMTG("Llanowar Elves", "Alpha", "Non Foil"));
