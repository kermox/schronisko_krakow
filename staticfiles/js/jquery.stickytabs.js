/**
 * jQuery Plugin: Sticky Bootstrap Tabs
 *
 * @author Aidan Lister <aidan@php.net>
 * @author Rocco Howard <rocco@bluora.com.au>
 */
function getOffset(el) {
    const rect = el.getBoundingClientRect();
    return {
        left: rect.left + window.scrollX,
        top: rect.top + window.scrollY
    };
}

(function ($) {
    $.fn.stickyTabs = function (options) {
        var context = this

        var settings = $.extend({
            getHashCallback: function (hash, btn) {
                return hash
            },
            selectorAttribute: "href",
            backToTop: false,
            showParentTabs: false,
            showTabUsingClickTrigger: false,
            initialTab: $('li.active > a', context),
            scrollToTab: '',
        }, options);

        // Show the tab corresponding with the hash in the URL, or the first tab.
        var showTabFromHash = function () {
            let hash = settings.selectorAttribute === "href" ? window.location.hash : window.location.hash.substring(1);
            if (hash !== '') {
                var selector = hash ? 'a[' + settings.selectorAttribute + '="' + hash + '"]' : settings.initialTab;
                if (settings.showParentTabs === true) {
                    showParentTabs(hash);
                }
                if (settings.showTabUsingClickTrigger === true) {
                    $(selector, context).trigger('click');
                } else {
                    $(selector, context).tab('show');
                    // When the hash is empty the desired tab is only showing, without scrolling to it.
                    // With scrollToTab variable it is possible to trigger scroll to desired element even with empty hash.
                    if (settings.scrollToTab){
                    window.scrollTo(settings.scrollToTab.position())
                    }

                }
                setTimeout(backToTop, 1);
            }
        }

        // Search upwards to select all parent tabs.
        var showParentTabs = function (hash) {
            parent_hash = $('a[' + settings.selectorAttribute + '="' + hash + '"]').parents('.tab-pane').attr('id');
            if (parent_hash !== undefined) {
                $('a[' + settings.selectorAttribute + '="#' + parent_hash + '"]').tab('show');
                showParentTabs('#' + parent_hash);
            }
        }

        // We use pushState if it's available so the page won't jump, otherwise a shim.
        var changeHash = function (hash) {
            if (history && history.pushState) {
                history.pushState(null, null, window.location.pathname + window.location.search + '#' + hash);
            } else {
                scrollV = document.body.scrollTop;
                scrollH = document.body.scrollLeft;
                window.location.hash = hash;
                document.body.scrollTop = scrollV;
                document.body.scrollLeft = scrollH;
            }
        }

        var backToTop = function () {
            if (settings.backToTop === true) {
                window.scrollTo(0, 0);
            }
        }

        // Set the correct tab when the page loads
        showTabFromHash();

        // Set the correct tab when a user uses their back/forward button
        $(window).on('hashchange', showTabFromHash);

        // Change the URL when tabs are clicked
        $('a', context).on('click', function (e) {
            var hash = this.href.split('#')[1];
            if (typeof hash != 'undefined' && hash !== '') {
                var adjustedhash = settings.getHashCallback(hash, this);
                changeHash(adjustedhash);
                setTimeout(backToTop, 1);
            }
        });

        return this;
    };
}(jQuery));
