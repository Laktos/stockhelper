//
//  Trade.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-25.
//

import Foundation

struct Trade: Hashable, Codable, Identifiable {
    var id: Int
    var name: String
    var transactions: Array<Transaction>
    var category: Category
    
    enum Category: String, CaseIterable, Codable {
        case open = "open"
        case closed = "closed"
    }
    
    var openDate: Date {
        let formatter = ISO8601DateFormatter()
        let datetime = formatter.date(from: transactions[0].buisday)
        return datetime!
    }
    var closeDate: Date {
        let formatter = ISO8601DateFormatter()
        let datetime = formatter.date(from: transactions.last!.buisday)
        return datetime!
    }
    
    var tradeValue: Int {
        var result: Double = 0.0
        if (category == .closed) {
            
        for transaction in transactions {
            
            if (transaction.transtype == "KÖPT") {
                result -= Double(transaction.qty)! * Double(transaction.price)!
            }
            if (transaction.transtype == "SÅLT") {
                result += Double(transaction.qty)! * Double(transaction.price)!
            }
        }
        }
        return Int(result)
        }
    
    
    var tradeValueString: String {
        return String(tradeValue)
    }
}
