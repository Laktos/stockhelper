//
//  TradeDetail.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-25.
//

import SwiftUI

struct TradeDetail: View {

    //vad händer ifall man inte hittar korrekt data? Vad vill jag ska hända?
    //Man bör ju inte få se grafer som inte har någon data. Man behöver kontrollera ifall StockInfo faktiskt har någon information, ifall den har det, kör TradingView-detail, annars, kör bara vanlig sammanställning av transaktionen och skriv att det inte finns någon data.
    @EnvironmentObject var modelData: ModelData
    @State var lookBack = 7
    @State var lookForward = 7
    
    var trade: Trade
    
    func getMatchingTradingviewData(_ stockName: String) -> StockInfo {
        if let data = modelData.tradingviewDict.first(where: {$0.name == stockName}) {
            return data
        } else {
            let defaultArray = [OnePeriodValues.init(
                ADX: "N/A",
                ATR: "N/A",
                Histogram: "N/A",
                MACD: "N/A",
                OnBalanceVolume: "N/A",
                RSI: "N/A",
                Volume: "N/A",
                baseLine: "N/A",
                bollingerbandspercentage: "N/A",
                close: "N/A",
                conversionLine: "N/A",
                dStoch: "N/A",
                date: "N/A",
                high: "N/A",
                kStoch: "N/A",
                laggingSpan: "N/A",
                leadOne: "N/A",
                leadTwo: "N/A",
                low: "N/A",
                moneyflow: "N/A",
                open: "N/A",
                signalMacd: "N/A",
                time: "N/A",
                volumeMa: "N/A")]
            let data = StockInfo(name: "N/A", data: defaultArray, id: "N/A")
            return data
        }
    }

    var stats: SimpleStatistics
    {
        return SimpleStatistics( trade: trade, lookBack: lookBack, lookForward: lookForward, stockInfo: getMatchingTradingviewData(trade.name))
    }
    
    var body: some View {
        
        VStack {
                ForEach(trade.transactions) { transaction in
                    HStack {
                        Text(transaction.price)
                        Text(transaction.qty)
                        Text(transaction.transtype)
                        Text(transaction.buisday)
                    }
                    .frame(width: 300)
                    .animation(.easeIn)
                    
                    
                }
            //Max 30 dagars lookback, men man måste kolla ifall det finns så gammal data, rangen bör begränsas av hur mycket data det finns. Om det inte finns någon måste man lägga in någon funktion för att hämta den datan. Men det är ett senare problem, tills vidare kan det göra att det inte går att presentera data.
            if (trade.closeDate - stats.stockInfo.data.last?.date)
            Stepper(value: $lookBack, in: 0..<) {
                
            }
//            VStack {
//                Text("Förändring 7 dagar efter försäljning")
//                HStack {
//                    Text("")
//                }
//            }
            }
        
        
        	
            
            
//                VStack {
//                    Text(stats.stockInfo.name)
//                    ForEach( 0..<stats.stockInfo.data.count ) { i in
//
//                        Text(stats.stockInfo.data[i].ADX)
//                    }
//
//
//                }
    }
}

struct TradeDetail_Previews: PreviewProvider {
    
    static let modelData = ModelData()
    static var previews: some View {
        TradeDetail(trade: modelData.trades[0])
            .environmentObject(modelData)
    }
}
