//
//  TradeRow.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-25.
//

import SwiftUI

struct TradeRow: View {
    var trade: Trade
    
    var body: some View {
        VStack(alignment: .leading) {
            
            HStack() {
                Text(trade.name)
                    .bold()
                if(trade.category == .closed) {
                    if(trade.tradeValue > 0) {
                        Text("\(trade.tradeValueString) kr")
                            .foregroundColor(.green)
                    }
                    else {
                        Text("\(trade.tradeValueString) kr")
                            .foregroundColor(.red)
                    }
                } else {
                    Image(systemName: "case.fill")
                }
            }
            HStack {
            Text(trade.transactions.first!.buisday)
                if(trade.category == .closed) {
                    Image(systemName: "arrow.forward")
                    Text(trade.transactions.last!.buisday)
                }
        }
    }
        .frame(minWidth: 230, minHeight: 45)
        .foregroundColor(.white)
        
}
}

struct TradeRow_Previews: PreviewProvider {
    static var trades = ModelData().trades
    
    static var previews: some View {
        Group {
        TradeRow(trade: trades[2])
        TradeRow(trade: trades[trades.count - 1])
        }
        .previewLayout(.fixed(width: 300, height: 70))
    }
}
