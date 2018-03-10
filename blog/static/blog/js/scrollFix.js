$.fn.scrollFix = function (opt) {
    var settings = opt;

    var $window = $(window),
        $this = $(this),
        windowHeight,
        scrollTop,
        thisHeight,
        $main = $(settings.main),
		$top = $(settings.top),
        mainHeight,
		bottomDis = 50;
    $window.scroll(function () {
        windowHeight = $window.height();
        scrollTop = $window.scrollTop();
        mainHeight = $main.outerHeight(true);
		topHeight = $top.outerHeight(true);
        $this.each(function (idx, val) {
            thisHeight = $(this).outerHeight(true);
            // 当主体区高度小于侧边栏时不做处理
            if (mainHeight < thisHeight) {
                return false;
            }
            // 当主体区高度大于侧边栏，且下滚高度+窗口高度大于侧边栏高度时，固定侧边栏
            if (scrollTop + windowHeight > topHeight + thisHeight + bottomDis) {
                $(this).css({
                    position: 'fixed',
                    bottom: bottomDis
                });
            } else {
                $(this).css({
                    position: 'static'
                });
            }
        });
    });

}