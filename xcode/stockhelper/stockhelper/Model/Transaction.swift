//
//  Transaction.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-25.
//

import Foundation

struct Transaction : Hashable, Codable, Identifiable {
    
    var id: String
    var buisday: String
    var liqday: String
    var transtype: String
    var name: String
    var instrumenttype: String
    var qty: String
    var price: String
    var fees: String
    var totvalue: String
    var forex: String
    var buytotvalue: String
    var result: String
    var totqty: String
    var balance: String
    var forexrate: String

}
