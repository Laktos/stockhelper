//
//  ModelData.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-25.
//

import Foundation
import Combine

final class ModelData: ObservableObject {
    @Published var trades: [Trade] = load("all_trades.json")
    @Published var tradingviewDict: [StockInfo] = load("downloaded_tradingview_data.json")
    
}

func load<T: Decodable>(_ filename: String) -> T {
    let data: Data

    guard let file = Bundle.main.url(forResource: filename, withExtension: nil)
        else {
            let script = Script()
            script.runScript("group_trades_to_json")
            fatalError("Couldn't find \(filename) in main bundle.")
            
    }

    do {
        data = try Data(contentsOf: file)
    } catch {
        fatalError("Couldn't load \(filename) from main bundle:\n\(error)")
    }

    do {
        let decoder = JSONDecoder()
        return try decoder.decode(T.self, from: data)
    } catch {
        fatalError("Couldn't parse \(filename) as \(T.self):\n\(error)")
    }
}

