//
//  ChartBar.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-28.
//

import SwiftUI

struct ChartBar: View {
    //Staplarna måste relateras till den högsta stapeln i grafen.
    //Finns exempel på detta i landmarks.
    var open : Double
    var close : Double
    var high : Double
    var low : Double
    
    var body: some View {
        ZStack {
            Rectangle()
                .fill()
                .frame(width: 20, height: 60)
                .offset()
            
        }
        
    }
}

struct ChartBar_Previews: PreviewProvider {
    static var previews: some View {
        ChartBar(open: 10.0, close: 15.0, high: 20.0, low: 5.0)
    }
}
