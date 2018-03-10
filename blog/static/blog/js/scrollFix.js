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
            // ���������߶�С�ڲ����ʱ��������
            if (mainHeight < thisHeight) {
                return false;
            }
            // ���������߶ȴ��ڲ���������¹��߶�+���ڸ߶ȴ��ڲ�����߶�ʱ���̶������
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