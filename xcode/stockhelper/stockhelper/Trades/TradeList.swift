//
//  TradeList.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-25.
//

import SwiftUI

struct TradeList: View {
    @EnvironmentObject var modelData: ModelData
    @State private var filter = FilterCategory.open
    @State private var selectedTrade: Trade?
    
    enum FilterCategory: String, CaseIterable, Identifiable {
        case all = "All"
        case closed = "closed"
        case open = "open"
        var id: FilterCategory { self }
    }
    
    var title: String {
        let title = filter == .all ? "Trades" : filter.rawValue
        return title
    }
    
    var trades: [Trade] {
        modelData.trades.filter { trade in
            (filter == .all||filter.rawValue == trade.category.rawValue)
        }
    }
    
//    var stockInfo: [StockInfo] {
//        modelData.tradingviewDict.filter { stock in
//            (stock.name == "ABB")
//        }
//    }
    
    var scriptsObj = Script()
    
    var body: some View {
     
        NavigationView {
            //Getting ADX info from the first
//            ForEach(stockInfo[0].data) { value in
//                Text()
//            }
            
            List {
                ForEach(trades) { trade in
                    NavigationLink(destination: TradeDetail(trade: trade)) {
                        TradeRow(trade: trade)
                    }
                }
            }
            .navigationTitle("Trades")
            .frame(minWidth: 250)
            .toolbar {
                ToolbarItem {
                    
                    Menu {
                        Picker("Category", selection: $filter) {
                            ForEach(FilterCategory.allCases) {
                                category in
                                Text(category.rawValue).tag(category)
                            }
                        }
                        .pickerStyle(InlinePickerStyle())
                    } label: {
                        Label("Category", systemImage: "slider.horizontal.3")
                    }
                }
                ToolbarItem {
                    Menu {
                        let labels = scriptsObj.scriptDict.map { $0.0 }
                        let paths = scriptsObj.scriptDict.map { $0.1 }
                        ForEach(labels.indices) {index in
                            Button(labels[index], action: { scriptsObj.runScript(paths[index]) })
                        }
                    } label: {
                        Label("Scripts", systemImage: "applescript")
                    }
                }
            }
            
        }
    }

}

struct TradeList_Previews: PreviewProvider {
    static var previews: some View {
        TradeList()
            .environmentObject(ModelData())
    }
}
