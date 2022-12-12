use std::error::Error;
use csv;

fn write_to_file(path: &str) -> Result<(), Box<dyn Error>> {
   let response = reqwest::blocking::get(
       "https://crypto.com/price",
   )
   .unwrap()
   .text()
   .unwrap();

   let document = scraper::Html::parse_document(&response);

   let title_selector = scraper::Selector::parse("table>tbody>tr td:nth-of-type(3) p.chakra-text").unwrap();
   let titles = document.select(&title_selector).map(|x| x.inner_html());

   let price_selector = scraper::Selector::parse("table>tbody>tr td:nth-of-type(4) .css-0").unwrap();
   let prices = document.select(&price_selector).map(|x| x.inner_html());

   let change_selector = scraper::Selector::parse("table>tbody>tr td:nth-of-type(5) p.chakra-text").unwrap();
   let changes = document.select(&change_selector).map(|x| x.inner_html());

   let volume_selector = scraper::Selector::parse("table>tbody>tr td:nth-of-type(6)").unwrap();
   let volumes = document.select(&volume_selector).map(|x| x.inner_html());

   let market_selector = scraper::Selector::parse("table>tbody>tr td:nth-of-type(7)").unwrap();
   let market = document.select(&market_selector).map(|x| x.inner_html());

   let mut titles_array = Vec::with_capacity(50);
   let mut prices_array = Vec::with_capacity(50);
   let mut changes_array = Vec::with_capacity(50);
   let mut volume_array = Vec::with_capacity(50);
   let mut market_array = Vec::with_capacity(50);
   titles
       .zip(1..50)
       .for_each(|(item, _)| titles_array.push(item));

   prices
       .zip(1..50)
       .for_each(|(item, _)| prices_array.push(item));

   changes
       .zip(1..50)
       .for_each(|(item, _)| changes_array.push(item));

   volumes
       .zip(1..50)
       .for_each(|(item, _)| volume_array.push(item));

   market
       .zip(1..50)
       .for_each(|(item, _)| market_array.push(item));

   let total = titles_array.len();
   let mut counter = 0;

   let mut writer = csv::Writer::from_path(path)?;
   writer.write_record(&["Title", "Price", "24HChange", "24hVolume", "MarketCap"])?;

   while counter < total {
       let a = &titles_array[counter];
       let b = &prices_array[counter];
       let c = &changes_array[counter];
       let d = &volume_array[counter];
       let e = &market_array[counter];

       println!("{}; {}; {}; {}; {}", a,b,c,d,e);
       writer.write_record(&[a,b,c,d,e])?;
       counter += 1;
   }

   writer.flush()?;
   Ok(())
}

fn main() {
   if let Err(e) = write_to_file("src/data.csv") {
       eprintln!("{}", e)
   }
}
