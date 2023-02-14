//
//  YWAutoCodeDataStore
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import "YWAutoCodeDataStore.h"


@interface YWAutoCodeDataStore ()
@property (nonatomic, strong) NSMutableArray *dataSource;

@end

@implementation YWAutoCodeDataStore


- (void)addData:(NSMutableArray *)data {
    [self.dataSource  addObjectsFromArray:data];
}
- (void)removeAllData {
    [self.dataSource  removeAllObjects];

}



@end
