//
//  StockHelperApp.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-25.
//

import SwiftUI

@main
struct StockHelperApp: App {
    @StateObject private var modelData = ModelData()
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(modelData)
        }
    }
}
