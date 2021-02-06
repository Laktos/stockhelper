//
//  SimpleStatistics.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-30.
//

import Foundation



struct SimpleStatistics {
    let trade: Trade
    var stockName : String {
        trade.name
    }
    let lookBack : Int
    let lookForward : Int
    
    let stockInfo : StockInfo

    var dateRange : ClosedRange<Int> {
        return getDateRange(lookBack, lookForward)
    }
    
    func getDateRange(_ lookBack: Int, _ lookForward: Int) -> ClosedRange<Int> {
        
        if(stockInfo.name == "N/A") {
            return (0...0)
        }
        
        let closeDate = trade.closeDate
        let openDate = trade.openDate
        
        let formatter = ISO8601DateFormatter()
        
        var fromIndex = 0
        var toIndex = 0
        
        for i in 0..<stockInfo.data.count {
            var datetime = formatter.date(from: stockInfo.data[i].date)
            if (datetime == openDate) {
                fromIndex = i
            }
            datetime = formatter.date(from: stockInfo.data[i].date)
            if(datetime == closeDate) {
                toIndex = i
            }
            
    }
        return (fromIndex...toIndex)
}
}
