//
//  StockInfo.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-28.
//

import Foundation

struct StockInfo: Hashable, Codable, Identifiable {
    var name : String
    var data : [OnePeriodValues]
    var id : String
}

struct OnePeriodValues : Hashable, Codable {
    var ADX : String
    var ATR : String
    var Histogram : String
    var MACD : String
    var OnBalanceVolume : String
    var RSI : String
    var Volume : String
    var baseLine : String
    var bollingerbandspercentage : String
    var close : String
    var conversionLine : String
    var dStoch : String
    var date : String
    var high : String
    var kStoch : String
    var laggingSpan : String
    var leadOne : String
    var leadTwo : String
    var low : String
    var moneyflow : String
    var open : String
    var signalMacd : String
    var time : String
    var volumeMa : String
}
