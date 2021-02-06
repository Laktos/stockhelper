//
//  Script.swift
//  StockHelper
//
//  Created by Albin Jonfelt on 2021-01-26.
//

import Foundation
import Python
import Automator

struct Script {
    
    let scriptDict = [("Pickle reset","hard_pickle_reset"), ("Download transactions", "download_transactions"), ("Download tradingview data", "download_tradingview_data")]
                      
                      
    func runScript(_ script: String) -> Void {
        print(script)
        let filePath = Bundle.main.url(forResource: script, withExtension: "workflow", subdirectory: "Automator")
        do {
            try AMWorkflow.run(at: filePath!, withInput: "")
        } catch {
            print(error)
        }
    }
    
}
