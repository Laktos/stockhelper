//
//  ContentView.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-25.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        TradeList()
            
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .environmentObject(ModelData())
    }
}
