//
//  YWAutoCodeDependencyFactory
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import "YWAutoCodeDependencyFactory.h"
#import "YWAutoCodeViewModel.h"
#import "YWAutoCodeController.h"
#import "YWAutoCodeDataStore.h"

@interface YWAutoCodeDependencyFactory ()

@end

@implementation YWAutoCodeDependencyFactory

+ (UIViewController*)createAutoCodeController{
    
    YWAutoCodeViewModel *viewModel = [[YWAutoCodeViewModel alloc] initWithDataStore:[YWAutoCodeDataStore new]];
    YWAutoCodeController *vc = [[YWAutoCodeController alloc] initWithViewModel:viewModel];
    return vc;
}


@end
